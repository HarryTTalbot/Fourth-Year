import FileDownloader from "./utils/fileDownloader";
import * as Imports from "./utils/imports";
import * as Path from "./utils/path";

export { FileDownloader, Imports, Path };

/**
 * Clamps a value to the specified minimum and maximum.
 * @param {number} val The value to clamp.
 * @param {number} min The minimum accepted value.
 * @param {number} max The maximum accepted value.
 * @returns The clamped value.
 */
export function clamp(val, min, max) {
  return Math.min(Math.max(val, min), max);
}
