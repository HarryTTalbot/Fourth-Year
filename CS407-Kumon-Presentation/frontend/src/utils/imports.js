import { FileTypeEnum } from "kumon_app_backend_api";

/**
 * Contains the various import types and their properties.
 */
export const IMPORT_TYPES = Object.freeze([
  { type: FileTypeEnum.Dumps, name: "Database Backup", file_ext: ".kumon" },
  { type: FileTypeEnum.KSis, name: "K-SIS Export", file_ext: ".xlsx" },
]);

/**
 * Gets the import type for the provided file.
 * @param {File | null} file The file we are attempting to import.
 * @returns {FileTypeEnum | null} The import type, or null if not a valid import file.
 */
export function getImportTypeForFile(file) {
  if (!file) {
    return null;
  }

  let im = IMPORT_TYPES.find((x) => file.name.endsWith(x.file_ext));
  return im?.type ?? null;
}

/**
 * Gets a human-readable name for the provided import type.
 * @param {FileTypeEnum} importType The type of import that was performed.
 * @returns {string} The name for the provided import type, or "Unknown Import Type" if invalid.
 */
export function getNameForImportType(importType) {
  let im = IMPORT_TYPES.find((x) => x.type === importType);
  return im?.name ?? "Unknown Import Type";
}
