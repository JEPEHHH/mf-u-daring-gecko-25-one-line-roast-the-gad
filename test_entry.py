"""Local gate and determinism tests for One-Line Roast (program/v1)."""

import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import main

REPO_ROOT = Path(__file__).resolve().parent


class TestEntryGate(unittest.TestCase):
    def test_default_output_path(self) -> None:
        self.assertEqual(main.DEFAULT_OUTPUT, Path("/output/entry.txt"))

    def test_license_present_and_mit(self) -> None:
        license_path = REPO_ROOT / "LICENSE"
        self.assertTrue(license_path.is_file(), "LICENSE file must exist at repo root")
        content = license_path.read_text(encoding="utf-8")
        self.assertIn("SPDX-License-Identifier: MIT", content)
        self.assertIn("MIT License", content)

    def test_gate_and_determinism_two_runs(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            out_a = Path(tmpdir) / "run1" / "entry.txt"
            out_b = Path(tmpdir) / "run2" / "entry.txt"

            for out_path in (out_a, out_b):
                proc = subprocess.run(
                    [sys.executable, str(REPO_ROOT / "main.py"), str(out_path)],
                    stdin=subprocess.DEVNULL,
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=10,
                )
                self.assertEqual(proc.returncode, 0, msg=f"stderr: {proc.stderr}")
                self.assertEqual(proc.stderr, "")
                self.assertTrue(out_path.is_file())
                self.assertFalse(out_path.is_symlink())

            raw_a = out_a.read_bytes()
            raw_b = out_b.read_bytes()

            # Determinism across two independent runs
            self.assertEqual(raw_a, raw_b)
            self.assertEqual(
                hashlib.sha256(raw_a).hexdigest(),
                hashlib.sha256(raw_b).hexdigest(),
            )

            # Valid UTF-8
            text = raw_a.decode("utf-8")

            # Gate checks: 1..200 chars, not only whitespace, strictly one line
            self.assertGreaterEqual(len(text), 1)
            self.assertLessEqual(len(text), 200)
            self.assertTrue(text.strip(), "Entry must not be whitespace only")
            self.assertEqual(text, text.strip(), "No leading or trailing whitespace")
            self.assertNotIn("\n", text)
            self.assertNotIn("\r", text)
            self.assertEqual(len(text.splitlines()), 1)

            # Plan conciseness target
            self.assertLessEqual(len(text), 140)


if __name__ == "__main__":
    unittest.main(verbosity=2)
