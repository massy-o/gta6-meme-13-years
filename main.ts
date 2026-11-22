// gta6-meme-x-01 hand-in program (Node 22, standard library only).
//
// The entry for this bounty is a post on X: a GTA 6 meme whose picture
// carries the make.fun ghost and whose text carries the bounty link and
// my play code. The house reads the post itself; all this program has
// to do is hand over POST.json, the file at the repository root that
// names the post's address, by copying it into the output directory.
//
// Local dry run:
//   MAKEFUN_OUTPUT_DIR=out node main.ts
// (MAKEFUN_BOT_DIR points at the repository when it is not /bot.)

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = join(botDir, 'POST.json');

if (!existsSync(source)) {
  console.error(`no POST.json found at ${source}`);
  process.exit(1);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, 'POST.json'));
console.log(`POST.json handed in from ${source}`);
