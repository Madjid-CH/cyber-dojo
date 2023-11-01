use geolocation::{Cardinal, Coordinates};
pub use geolocation::Grid;

mod geolocation;


pub struct Rover {
    cardinal: Cardinal,
    coordinates: Coordinates,
    grid: Grid,
}

impl Rover {
    pub fn new(grid: Grid) -> Self {
        Self {
            cardinal: Cardinal::North,
            coordinates: Coordinates::new(),
            grid,
        }
    }

    pub fn execute(&mut self, commands: &str) -> String {
        for command in commands.chars() {
            match command {
                'R' => self.cardinal = self.cardinal.right(),
                'L' => self.cardinal = self.cardinal.left(),
                'M' => match self.move_forward() {
                    Ok(new_coord) => self.coordinates = new_coord,
                    Err(_) => return format!("O:{}:{}", self.coordinates, self.cardinal),
                },
                _ => panic!("Unknown command {}", command),
            }
        }
        format!("{}:{}", self.coordinates, self.cardinal)
    }

    fn move_forward(&mut self) -> Result<Coordinates, ()> {
        let new_coord = self.coordinates.move_forward(&self.cardinal);
        if self.grid.is_obstacle(&new_coord) {
            return Err(());
        }
        Ok(new_coord)
    }
}