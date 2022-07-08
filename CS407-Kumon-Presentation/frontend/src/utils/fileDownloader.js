/**
 * Helper class for downloading files from the backend API.
 */
export default class FileDownloader {
  constructor() {}

  /**
   * Initiates a file download using a JavaScript blob and the provided file name.
   * @param {Blob} blob The file to download.
   * @param {string} filename The suggested file name.
   */
  downloadBlob(blob, filename) {
    let link = document.createElement("a");
    link.download = filename;
    link.href = URL.createObjectURL(blob);
    link.click();

    URL.revokeObjectURL(link.href);
  }
}
