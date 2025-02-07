
from main import get_slot_machine_spin, ROWS, COLS, symbol_count  # Importez ce que vous voulez tester

def test_get_slot_machine_spin_returns_correct_structure():
    """
    Test que get_slot_machine_spin retourne une liste de colonnes,
    et que chaque colonne a le bon nombre de lignes.
    """
    columns = get_slot_machine_spin(ROWS, COLS, symbol_count)
    assert isinstance(columns, list), "get_slot_machine_spin doit retourner une liste"
    assert len(columns) == COLS, "Nombre de colonnes incorrect"
    for column in columns:
        assert isinstance(column, list), "Chaque colonne doit être une liste"
        assert len(column) == ROWS, "Nombre de lignes incorrect dans une colonne"

