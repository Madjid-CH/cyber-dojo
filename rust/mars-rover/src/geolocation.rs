use std::fmt::{Display, Formatter};

const GRID_SIZE: u8 = 10;

#[derive(PartialEq, Eq)]
pub struct Coordinates {
    x: u8,
    y: u8,
}


impl Coordinates {

    pub fn new() -> Self {
        Self { x: 0, y: 0 }
    }
    pub(crate) fn move_forward(&self, cardinal: &Cardinal) -> Self {
        match cardinal {
            Cardinal::North => Self {
                x: self.x,
                y: (self.y + 1) % GRID_SIZE,
            },
            Cardinal::East => Self {
                x: (self.x + 1) % GRID_SIZE,
                y: self.y,
            },
            Cardinal::West => Self {
                x: (self.x + (GRID_SIZE - 1)) % GRID_SIZE,
                y: self.y,
            },
            Cardinal::South => Self {
                x: self.x,
                y: (self.y + (GRID_SIZE - 1)) % GRID_SIZE,
            },
        }
    }
}

impl Display for Coordinates {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}:{}", self.x, self.y)
    }
}

pub enum Cardinal {
    North,
    East,
    South,
    West,
}

impl Cardinal {
    pub(crate) fn right(&self) -> Self {
        match self {
            Cardinal::North => Cardinal::East,
            Cardinal::East => Cardinal::South,
            Cardinal::South => Cardinal::West,
            Cardinal::West => Cardinal::North,
        }
    }

    pub(crate) fn left(&self) -> Self {
        match self {
            Cardinal::North => Cardinal::West,
            Cardinal::East => Cardinal::North,
            Cardinal::South => Cardinal::East,
            Cardinal::West => Cardinal::South,
        }
    }
}

impl Display for Cardinal {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", match self {
            Cardinal::North => "N",
            Cardinal::East => "E",
            Cardinal::South => "S",
            Cardinal::West => "W",
        })
    }
}

pub struct Grid {
    size: u8,
    obstacles: Vec<Coordinates>,
}

impl Grid {
    pub fn new() -> Self {
        Self {
            size: GRID_SIZE,
            obstacles: vec![],
        }
    }

    pub fn with_obstacles(obstacles: Vec<(u8, u8)>) -> Self {
        Self {
            size: GRID_SIZE,
            obstacles: obstacles.into_iter().map(|(x, y)| Coordinates { x, y }).collect(),
        }
    }

    pub fn is_obstacle(&self, coordinates: &Coordinates) -> bool {
        self.obstacles.contains(coordinates)
    }
}