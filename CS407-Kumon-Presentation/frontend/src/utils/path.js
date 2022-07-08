/**
 * Gets the basename from a file path.
 * @param {string} path The path to get the basename from.
 */
export function basename(path) {
  return path.split(/[\\/]/).pop();
}
