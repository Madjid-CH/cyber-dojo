use mars_rover::{Grid, Rover};

fn main() {
    let mut rover = Rover::new(Grid::new());
    let position = rover.execute("MMRMMLM");
    println!("End position: {}", position);
}