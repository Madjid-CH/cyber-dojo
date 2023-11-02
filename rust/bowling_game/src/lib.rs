#![cfg_attr(feature = "strict", deny(warnings))]

fn parse_input(input: &str) -> Vec<u32> {
    let input: Vec<_> = input.split("||").collect();
    let (main_throws, bonus_throws) = (input[0], input[1]);
    let frames = main_throws.split("|");
    let mut result = Vec::new();
    for frame in frames {
        result.extend(parse_frame(frame));
    }
    result.extend(parse_bonus_throws(bonus_throws));
    result
}

fn parse_bonus_throws(throws: &str) -> Vec<u32> {
    throws
        .chars()
        .map(parse_throw)
        .collect::<Vec<_>>()
}

fn parse_frame(frame: &str) -> Vec<u32> {
    if frame == "X" {
        return vec![10, 0];
    }
    let frame = frame.chars().collect::<Vec<_>>();
    let first_throw = parse_throw(frame[0]);
    let second_throw = if frame[1] == '/' {
        10 - first_throw
    } else {
        parse_throw(frame[1])
    };
    return vec![first_throw, second_throw];
}

fn parse_throw(throw: char) -> u32 {
    match throw {
        'X' => 10,
        '-' => 0,
        _ => throw.to_digit(10).unwrap()
    }
}

fn score(throws: Vec<u32>) -> u32 {
    let mut score = 0;
    for i in 0..10 {
        if is_strike(&throws, i) {
            score += strike_score(&throws, i);
        } else if is_spare(&throws, i) {
            score += spare_score(&throws, i);
        } else {
            score += open_frame_score(&throws, i);
        }
    }
    score
}

fn is_strike(throws: &Vec<u32>, i: usize) -> bool {
    throws[i * 2] == 10
}

fn is_spare(throws: &Vec<u32>, i: usize) -> bool {
    throws[i * 2] + throws[i * 2 + 1] == 10
}

fn spare_score(throws: &Vec<u32>, i: usize) -> u32 {
    throws[i * 2] + throws[i * 2 + 1] + throws[i * 2 + 2]
}

fn open_frame_score(throws: &Vec<u32>, i: usize) -> u32 {
    throws[i * 2] + throws[i * 2 + 1]
}

fn strike_score(throws: &Vec<u32>, i: usize) -> u32 {
    let score = throws[i * 2] + throws[i * 2 + 2] + throws[i * 2 + 3];
    if i * 2 + 4 < throws.len() && throws[i * 2 + 2] == 10 {
        return score + throws[i * 2 + 4];
    }
    score
}


#[cfg(test)]
mod tests {
    use parameterized::parameterized;

    use super::*;

    static GETTER_GAME: &str = "--|--|--|--|--|--|--|--|--|--||";
    static PERFECT_GAME: &str = "X|X|X|X|X|X|X|X|X|X||XX";
    static ALL_NINES_GAME: &str = "9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||";
    static ALL_SPARES_GAME: &str = "5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5";

    #[test]
    fn it_parse_strike() {
        let frame = "X";
        assert_eq!(parse_frame(frame), vec![10, 0]);
    }

    #[parameterized(spare = { "5/", "7/" }, expected = { vec ! [5, 5], vec ! [7, 3]})]
    fn it_parse_spare(spare: &str, expected: Vec<u32>) {
        assert_eq!(parse_frame(spare), expected);
    }

    #[test]
    fn it_parse_open_throw() {
        let frame = "45";
        assert_eq!(parse_frame(frame), vec![4, 5]);
    }

    #[test]
    fn it_parse_misses() {
        let frame = "--";
        assert_eq!(parse_frame(frame), vec![0, 0]);
    }


    #[parameterized(
    input = { PERFECT_GAME, ALL_NINES_GAME, ALL_SPARES_GAME },
    expected = {
    vec ! [10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 10],
    vec ! [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
    vec ! [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    })]
    fn it_should_parse_input(input: &str, expected: Vec<u32>) {
        assert_eq!(parse_input(input), expected);
    }

    #[test]
    fn score_gutter_game() {
        let input = parse_input(GETTER_GAME);
        assert_eq!(score(input), 0);
    }

    #[test]
    fn score_all_nines_game() {
        let input = parse_input(ALL_NINES_GAME);
        assert_eq!(score(input), 90);
    }

    #[test]
    fn score_all_spares() {
        let input = parse_input(ALL_SPARES_GAME);
        assert_eq!(score(input), 150);
    }

    #[test]
    fn score_perfect_game() {
        let input = parse_input(PERFECT_GAME);
        assert_eq!(score(input), 300);
    }

    #[test]
    fn acceptance_test() {
        let input = parse_input("X|7/|9-|X|-8|8/|-6|X|X|X||81");
        assert_eq!(score(input), 167);
    }
}
