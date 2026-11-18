# Roblox AI Creator Toolkit

Early-stage open-source toolkit for independent Roblox developers and content creators. The current prototype runs locally, without an API key or subscription. AI integrations are planned, not implemented.

## Current features

- **Luau review helper:** flags selected patterns that merit manual security review, including dynamic code, numeric module dependencies, HTTP calls and server remote events. This is a regex-based heuristic, not a comprehensive vulnerability scanner; it can produce false positives and miss real issues.
- **Creator planner:** produces a structured long-video and Shorts planning template, with an originality and audience-suitability checklist.
- **Roblox rate limiter:** sample server-side ModuleScript for per-player action cooldowns. Remove player entries on `Players.PlayerRemoving`; always validate server-side permissions and payloads independently. The module has not been tested in Roblox Studio.

## Quick start

Python 3.10 or newer; no third-party packages.

```sh
python toolkit.py scan roblox
python toolkit.py plan "A space adventure"
python -m unittest discover -s tests -v
```

## Roadmap

- Add parser-aware Luau review and Roblox Studio tests.
- Explore optional AI-assisted code review and content planning with explicit approval before sending source material to external services.
- Improve contributions, documentation and examples based on real developer feedback.

## Contributions

Open an issue with a reproducible example or submit a patch with tests. Do not include secrets, private player information or copyrighted assets without permission.

This project is independent and is not affiliated with Roblox or OpenAI.
