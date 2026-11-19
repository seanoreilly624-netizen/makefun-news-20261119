// Entry program for the 19 November 2026 world-news image.
//
// The image itself is drawn ahead of time by build_image.py and shipped in
// this repository as entry.png. All this program does is place that file
// into the output directory the grader hands it. It needs no network and
// draws nothing at run time, so both graded runs write identical bytes.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = join(here, "entry.png");

// Refuse to ship a file that is not a PNG: a truncated or wrong-format
// image would fail the gate, so fail here instead, loudly.
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!readFileSync(source).subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error("entry.png is not a PNG file");
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, "entry.png"));
