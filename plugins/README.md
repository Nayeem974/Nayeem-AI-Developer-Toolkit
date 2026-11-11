# Optional Claude Code plugins

The folders here preserve upstream plugin sources, including hooks, commands, agents, scripts, and references. Install only what you need. Plugin installation can execute hooks or add capabilities, so inspect permissions and upstream release notes first.

From Claude Code, add each local marketplace (run from the toolkit's extracted directory; absolute paths are safest):

```bash
claude plugin marketplace add /absolute/path/to/Nayeem-AI-Developer-Toolkit/plugins/superpowers
claude plugin marketplace add /absolute/path/to/Nayeem-AI-Developer-Toolkit/plugins/ponytail
claude plugin marketplace add /absolute/path/to/Nayeem-AI-Developer-Toolkit/plugins/vibe-wise
claude plugin marketplace add /absolute/path/to/Nayeem-AI-Developer-Toolkit/plugins/impeccable
```

Then install the plugins from their marketplace names (if the local marketplace registration succeeds):

```text
/plugin install superpowers@superpowers-dev
/plugin install ponytail@ponytail
/plugin install vibe-wise@vibe-wise
/plugin install impeccable@impeccable-local
```

If Claude Code reports a different marketplace identifier, use the exact name shown by `/plugin marketplace list`. Restart Claude Code after installation.

## Recommended activation
- **Install first:** Superpowers. Use for brainstorming, plans, TDD, systematic debugging, code review, and verification.
- **Install next:** Impeccable. Use its `/impeccable` commands for frontend critique, audit, and polish.
- **Install optionally:** Ponytail. It encourages simpler implementations. Review its hooks/settings before enabling any telemetry or webhook; keep webhook URL blank unless intentionally configured.
- **Install optionally:** VibeWise. Activate `/vibe-wise:learn` only when you want a learning-first session. It intentionally asks for your approach and may conflict with your default AI-does-most-coding workflow.

Do not install the archived Claude Memory plugin. Use Claude Code's native auto-memory; the archived package is retained under `references/archived-claude-memory/` for its decision-tree reference only.

## Compatibility notes
- These are upstream plugin source snapshots, not a guarantee of compatibility with every Claude Code version. Check plugin manifests and current upstream documentation before enabling.
- Impeccable's marketplace manifest was added by this toolkit as a local wrapper; the upstream ZIP supplied plugin metadata but no marketplace manifest.
- VibeWise and Superpowers have upstream Claude plugin metadata. Ponytail has upstream Claude plugin metadata.
