use serialize::serialize_board;
use validity::is_valid_board;

mod serialize;
mod validity;

pub fn n_queens(n: usize) -> Vec<Vec<String>> {
    let mut frontier: Vec<Vec<Option<usize>>> = generate_initial_search_boards(n);
    let mut results: Vec<Vec<Option<usize>>> = vec![];
    while !frontier.is_empty() {
        if let Some(board) = search(n, &mut frontier) {
            results.push(board);
        }
    }
    format_results(results)
}

fn generate_initial_search_boards(n: usize) -> Vec<Vec<Option<usize>>> {
    let mut frontier: Vec<Vec<Option<usize>>> = vec![];
    for row in 0..n {
        let mut board: Vec<Option<usize>> = (0..n).map(|_| None).collect();
        board[0] = Some(row);
        frontier.push(board);
    }
    frontier
}

fn search(n: usize, frontier: &mut Vec<Vec<Option<usize>>>) -> Option<Vec<Option<usize>>> {
    let board = frontier.pop().unwrap();
    let number_of_complete_columns = board.iter()
        .filter(|col| col.is_some())
        .count();
    let index_of_latest_added_queen = number_of_complete_columns - 1;

    if n != 1 {
        for row in 0..n {
            let mut new_board = board.clone();
            new_board[index_of_latest_added_queen + 1] = Some(row);

            if is_valid_board(&new_board) {
                if number_of_complete_columns + 1 == n {
                    return Some(new_board);
                } else {
                    frontier.push(new_board);
                }
            }
        }
    } else {
        return Some(board);
    }
    None
}

fn format_results(results: Vec<Vec<Option<usize>>>) -> Vec<Vec<String>> {
    results.iter()
        .map(|board| board.iter()
            .map(|col| col.unwrap())
            .collect::<Vec<usize>>())
        .map(|board| serialize_board(&board))
        .collect()
}
