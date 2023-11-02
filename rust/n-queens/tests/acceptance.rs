use n_queens::n_queens;

#[test]
fn given_n_1_should_return_1_solution() {
    let result = n_queens(1);
    assert_eq!(result, vec![
        vec!["Q"]
    ])
}

#[test]
fn given_n_2_should_return_no_solutions() {
    let result = n_queens(2);
    let expected: Vec<Vec<String>> = vec![];
    assert_eq!(result, expected)
}

#[test]
fn given_n_4_should_return_2_solutions() {
    let result = n_queens(4);
    assert_eq!(result, vec![
        vec![".Q..",
             "...Q",
             "Q...",
             "..Q."],
        vec!["..Q.",
             "Q...",
             "...Q",
             ".Q.."],
    ])
}

#[test]
fn given_n_8_should_return_92_solutions() {
    let result = n_queens(8);
    assert_eq!(result.len(), 92)

}