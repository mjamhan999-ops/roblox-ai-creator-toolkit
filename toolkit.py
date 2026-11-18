"""Local, dependency-free creator utilities. Python 3.10+."""
import argparse
import json
import re
from pathlib import Path

RULES = {
    'dynamic-code': (r'\bloadstring\s*\(', 'Review dynamic code execution.'),
    'remote-module': (r'\brequire\s*\(\s*\d+\s*\)', 'Review third-party numeric asset dependencies.'),
    'remote-event': (r'\.OnServerEvent\s*:\s*Connect\s*\(', 'Check server-side authorization, validation and rate limits.'),
    'http-request': (r':\s*(?:RequestAsync|PostAsync|GetAsync)\s*\(', 'Review URLs, secrets and data handling.'),
}

def scan(root):
    findings = []
    paths = [root] if root.is_file() else sorted(root.rglob('*'))
    for path in paths:
        if path.suffix.lower() not in ('.lua', '.luau') or not path.is_file():
            continue
        for line_no, line in enumerate(path.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
            if line.lstrip().startswith('--'):
                continue
            for key, (pattern, message) in RULES.items():
                if re.search(pattern, line):
                    findings.append({'file': str(path), 'line': line_no, 'rule': key, 'message': message})
    return findings

def plan(topic):
    topic = ' '.join(topic.split())
    if not topic:
        raise ValueError('Topic must not be empty')
    return {'topic': topic, 'long_video': {'hook': f'Introduce {topic} with a clear visual question.', 'beats': ['Introduce the goal', 'Show three steps', 'Resolve the challenge', 'Recap the lesson']}, 'shorts': [{'idea': 'Show the most engaging moment', 'duration_seconds': 25}, {'idea': 'Show a before-and-after or quick tip', 'duration_seconds': 20}], 'review': ['Check originality and asset licenses', 'Verify audience suitability', 'Review captions and audio', 'Remove personal information']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    s = sub.add_parser('scan'); s.add_argument('path', type=Path)
    p = sub.add_parser('plan'); p.add_argument('topic')
    args = parser.parse_args()
    if args.command == 'scan':
        if not args.path.exists(): parser.error('Path does not exist')
        result = scan(args.path)
    else:
        try: result = plan(args.topic)
        except ValueError as exc: parser.error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
