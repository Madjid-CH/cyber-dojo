use rstest::rstest;

use mars_rover::{Grid, Rover};

#[test]
fn initial_position_at_origin_facing_north() {
    let mut rover = Rover::new(Grid::new());
    let position = rover.execute("");
    assert_eq!(position, "0:0:N")
}

#[rstest]
#[case::rotate_to_east("R", 'E')]
#[case::rotate_to_south("RR", 'S')]
#[case::rotate_to_west("RRR", 'W')]
#[case::rotate_to_east("RRRR", 'N')]
#[case::rotate_back_to_east("RRRRR", 'E')]
fn it_rotates_to_the_right(#[case] commands: &str, #[case] cardinal: char) {
    let mut rover = Rover::new(Grid::new());
    let position = rover.execute(commands);
    assert_eq!(position, format!("0:0:{cardinal}"))
}

#[rstest]
#[case::rotate_to_west("L", 'W')]
#[case::rotate_to_south("LL", 'S')]
#[case::rotate_to_east("LLL", 'E')]
#[case::rotate_to_west("LLLL", 'N')]
#[case::rotate_back_to_west("LLLLL", 'W')]
fn it_rotates_to_the_left(#[case] commands: &str, #[case] cardinal: char) {
    let mut rover = Rover::new(Grid::new());
    let position = rover.execute(commands);
    assert_eq!(position, format!("0:0:{cardinal}"))
}

#[rstest]
#[case::one_north("M", "0:1:N")]
#[case::two_north("MM", "0:2:N")]
#[case::eleven_north("MMMMMMMMMM", "0:0:N")]
#[case::east("RM", "1:0:E")]
#[case::east("RMMMMMMMMMMM", "1:0:E")]
#[case::west("LM", "9:0:W")]
#[case::west("LMMMMMMMMM", "1:0:W")]
#[case::south("RRM", "0:9:S")]
#[case::south("RRMM", "0:8:S")]
#[case::south("RRMMMMMMMMMM", "0:0:S")]
fn it_moves_forward(#[case] commands: &str, #[case] expected_position: &str) {
    let mut rover = Rover::new(Grid::new());
    let position = rover.execute(commands);
    assert_eq!(position, expected_position)

}

#[test]
fn it_detects_obstacles() {
    let grid = Grid::with_obstacles(vec![(0, 3), (5, 0)]);
    let mut rover = Rover::new(grid);
    let position = rover.execute("MMMM");
    assert_eq!(position, "O:0:2:N")
}
