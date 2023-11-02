pub fn is_valid_board(board: &Vec<Option<usize>>) -> bool {
    let number_of_complete_columns = board.iter()
        .filter(|col| col.is_some())
        .count();

    let newest_queen_x_position = number_of_complete_columns - 1;
    let newest_queen_y_position = board[number_of_complete_columns - 1].unwrap();
    for x in 0..newest_queen_x_position {
        let y = board[x].unwrap();
        if y == newest_queen_y_position {
            return false;
        }
        let x_diff = newest_queen_x_position.abs_diff(x);
        let y_diff = newest_queen_y_position.abs_diff(y);
        if x_diff == y_diff {
            return false
        }
    }

    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn single_tile_board_is_valid() {
        let board = vec![Some(0)];
        let result = is_valid_board(&board);
        assert!(result);
    }

    #[test]
    fn given_horizontally_adjacent_queens_should_return_invalid() {
        let board = vec![Some(1), Some(3), Some(0), Some(0)];
        let result = is_valid_board(&board);
        assert!(!result);
    }

    #[test]
    fn given_far_horizontally_adjacent_queen_on_incomplete_board_should_be_invalid() {
        let board = vec![Some(1), Some(3), Some(1), None];
        let result = is_valid_board(&board);
        assert!(!result);
    }

    #[test]
    fn given_diagonally_adjacent_queens_should_return_invalid() {
        let board = vec![Some(0), Some(1), None, None];
        let result = is_valid_board(&board);
        assert!(!result);
    }

    #[test]
    fn given_complete_valid_board_should_return_valid() {
        let board = vec![Some(1), Some(3), Some(0), Some(2)];
        let result = is_valid_board(&board);
        assert!(result);
    }
    
    #[test]
    fn given_far_diagonally_adjacent_queens_return_invalid() {
        let board = vec![Some(0), Some(0), Some(2), None];
        assert!(!is_valid_board(&board));
    }
    
    #[test]
    fn given_reverse_diagonally_adjacent_queens_return_invalid() {
        let board = vec![Some(2), Some(2), Some(0), None];
        assert!(!is_valid_board(&board));
    }
}