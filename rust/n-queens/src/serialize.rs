pub fn serialize_board(board: &Vec<usize>) -> Vec<String> {
    let mut result = vec![];
    for column_index in 0..board.len() {
        let row_index = get_row_index(&board, &column_index);
        let row = get_row_with_queen(&board, row_index);
        result.push(row);
    }
    result
}

fn get_row_index(board: &Vec<usize>, column_index: &usize) -> usize {
    board.iter()
        .enumerate()
        .filter(|(_x, y)| y == &column_index)
        .last()
        .unwrap().0
}

fn get_row_with_queen(board: &Vec<usize>, xx: usize) -> String {
    let mut row = String::new();
    for x in 0..board.len() {
        if x == xx {
            row.push('Q');
        } else {
            row.push('.');
        }
    }
    row
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_size_board() {
        let board = vec![0];
        let result = serialize_board(&board);
        assert_eq!(result, vec!["Q"]);
    }

    #[test]
    fn four_size_board() {
        let board = vec![1, 3, 0, 2];
        let result = serialize_board(&board);
        assert_eq!(result, vec![
            "..Q.",
            "Q...",
            "...Q",
            ".Q.."
        ]);
    }
}