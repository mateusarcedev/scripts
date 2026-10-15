import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "subtitles" / "convert_srt_to_4k_ass.py"
spec = importlib.util.spec_from_file_location("convert_srt_to_4k_ass", SCRIPT)
conv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(conv)


def dialogues(ass):
    return [line for line in ass.splitlines() if line.startswith("Dialogue:")]


class SrtToAssTest(unittest.TestCase):
    def test_converts_timecodes_to_centiseconds(self):
        ass = conv.srt_to_ass("1\n00:00:01,000 --> 00:00:02,999\nOi\n")
        self.assertEqual(dialogues(ass), ["Dialogue: 0,0:00:01.00,0:00:02.99,Default,,0,0,0,,Oi"])

    def test_accepts_arrow_without_spaces_and_missing_millis(self):
        ass = conv.srt_to_ass("1\n01:02:03-->01:02:04,5\nOi\n")
        self.assertEqual(dialogues(ass), ["Dialogue: 0,1:02:03.00,1:02:04.50,Default,,0,0,0,,Oi"])

    def test_joins_multiline_text_and_handles_crlf_and_bom(self):
        ass = conv.srt_to_ass("﻿1\r\n00:00:01,000 --> 00:00:02,000\r\nlinha 1\r\nlinha 2\r\n\r\n")
        self.assertTrue(dialogues(ass)[0].endswith(",linha 1\\Nlinha 2"))

    def test_escapes_braces_and_converts_format_tags(self):
        ass = conv.srt_to_ass('1\n00:00:01,000 --> 00:00:02,000\n<i>Olá</i> {x} <font color="red">y</font>\n')
        self.assertTrue(dialogues(ass)[0].endswith(",{\\i1}Olá{\\i0} \\{x\\} y"))

    def test_rejects_invalid_timecode(self):
        with self.assertRaises(conv.SrtError):
            conv.srt_to_ass("1\n00:00:01 -> 00:00:02\n00:01 --> 00:02\nOi\n")

    def test_rejects_file_without_cues(self):
        with self.assertRaises(conv.SrtError):
            conv.srt_to_ass("texto qualquer\n")


class MainTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.srt = self.dir / "legenda.srt"

    def tearDown(self):
        self.tmp.cleanup()

    def run_main(self, *args):
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            try:
                return conv.main([str(a) for a in args])
            except SystemExit as e:
                return e.code

    def test_writes_ass_next_to_input_by_default(self):
        self.srt.write_text("1\n00:00:01,000 --> 00:00:02,000\nOi\n", encoding="utf-8")
        self.assertEqual(self.run_main(self.srt), 0)
        self.assertIn("PlayResX: 3840", (self.dir / "legenda.ass").read_text(encoding="utf-8"))

    def test_does_not_overwrite_without_force(self):
        self.srt.write_text("1\n00:00:01,000 --> 00:00:02,000\nOi\n", encoding="utf-8")
        out = self.dir / "legenda.ass"
        out.write_text("existente", encoding="utf-8")
        self.assertNotEqual(self.run_main(self.srt), 0)
        self.assertEqual(out.read_text(encoding="utf-8"), "existente")
        self.assertEqual(self.run_main(self.srt, "--force"), 0)
        self.assertNotEqual(out.read_text(encoding="utf-8"), "existente")

    def test_invalid_input_leaves_no_output(self):
        self.srt.write_text("1\n00:00:01,000 --> 00:00:02,000\nOi\n\n2\n00:01 --> 00:02\nx\n", encoding="utf-8")
        self.assertEqual(self.run_main(self.srt), 1)
        self.assertFalse((self.dir / "legenda.ass").exists())

    def test_missing_input_fails(self):
        self.assertNotEqual(self.run_main(self.dir / "nao-existe.srt"), 0)


if __name__ == "__main__":
    unittest.main()
