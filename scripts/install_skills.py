#!/usr/bin/env python3
"""Install the curated skill library and project instructions."""
import argparse, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "claude": (".claude/skills", Path.home()/".claude"/"skills"),
    "codex": (".agents/skills", Path.home()/".agents"/"skills"),
    "opencode": (".agents/skills", Path.home()/".agents"/"skills"),
    "cursor": (".cursor/skills", Path.home()/".cursor"/"skills"),
}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--target', choices=TARGETS, required=True)
    ap.add_argument('--scope', choices=['project','user'], default='project')
    ap.add_argument('--project', type=Path, default=Path.cwd())
    ap.add_argument('--force', action='store_true', help='Replace existing skill folders')
    args=ap.parse_args()
    rel, user_path=TARGETS[args.target]
    dest=(args.project.resolve()/rel) if args.scope=='project' else user_path
    dest.mkdir(parents=True,exist_ok=True)
    count=0; skipped=[]
    for src in sorted((ROOT/'skills').iterdir()):
        if not src.is_dir() or not (src/'SKILL.md').exists(): continue
        target=dest/src.name
        if target.exists():
            if not args.force:
                skipped.append(src.name); continue
            shutil.rmtree(target)
        shutil.copytree(src,target)
        count+=1
    if args.scope=='project':
        project=args.project.resolve(); project.mkdir(parents=True,exist_ok=True)
        for name in ['AGENTS.md','CLAUDE.md','SKILL-ROUTER.md','MASTER-DEVELOPMENT-PROMPT.md']:
            src=ROOT/name; target=project/name
            if target.exists() and not args.force:
                skipped.append(name); continue
            shutil.copy2(src,target)
    print(f'Installed {count} skills to {dest}')
    if skipped: print('Kept existing (not overwritten): '+', '.join(skipped))
    print('Optional plugins are NOT installed automatically. See plugins/README.md.')
if __name__=='__main__': main()
