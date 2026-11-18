import tempfile
import unittest
from pathlib import Path
from toolkit import scan, plan

class ToolkitTests(unittest.TestCase):
    def test_scan_flags_dynamic_code_and_remote_events(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'sample.luau'
            p.write_text('-- loadstring(x)\nloadstring(x)\nevent.OnServerEvent:Connect(fn)\nrequire(123)\n', encoding='utf-8')
            self.assertEqual([f['rule'] for f in scan(Path(tmp))], ['dynamic-code', 'remote-event', 'remote-module'])
    def test_clean_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'sample.lua'; p.write_text('return 42', encoding='utf-8')
            self.assertEqual(scan(p), [])
    def test_plan(self):
        self.assertEqual(plan('  Space   adventure ')['topic'], 'Space adventure')
        self.assertEqual(len(plan('Space')['shorts']), 2)
    def test_empty_topic(self):
        with self.assertRaises(ValueError): plan(' ')

if __name__ == '__main__': unittest.main()
