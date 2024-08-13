__app_name__ = "smart-shell"
__version__ = "0.1.0"

# TODO: edit or remove

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    WRITE_ERROR: "model config write error",
    ID_ERROR: "to-do id error",
}