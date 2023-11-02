use std::collections::HashMap;
use std::iter::zip;

use crate::Coin::*;

#[derive(Hash, PartialEq, Eq, Debug)]
enum Coin {
    Quarter,
    Dime,
    Nickel,
    Penny,
}

impl Coin {
    fn value(&self) -> usize {
        match self {
            Quarter => 25,
            Dime => 10,
            Nickel => 5,
            Penny => 1,
        }
    }
}

fn make_changes(cents: usize) -> Vec<HashMap<Coin, usize>> {
    if cents == 0 {
        return vec![];
    }
    let mut changes = vec![];
    for n_quarter in (0..=cents / Quarter.value()).rev() {
        let quarter_remaining = cents - n_quarter * Quarter.value();
        for n_dime in (0..=quarter_remaining / Dime.value()).rev() {
            let dim_remaining = quarter_remaining - n_dime * Dime.value();
            for n_nickle in (0..=dim_remaining / Nickel.value()).rev() {
                let n_pinnies = dim_remaining - n_nickle * Nickel.value();
                changes.push(make_change(n_quarter, n_dime, n_nickle, n_pinnies));
            }
        }
    }
    changes
}

fn make_change(
    n_quarter: usize,
    n_dime: usize,
    n_nickle: usize,
    n_pinnies: usize,
) -> HashMap<Coin, usize> {
    let mut change = HashMap::new();
    for (c, n) in zip(
        [Quarter, Dime, Nickel, Penny],
        [n_quarter, n_dime, n_nickle, n_pinnies],
    ) {
        if n != 0 {
            change.insert(c, n);
        }
    };
    change
}

#[cfg(test)]
mod tests {
    use test_case::test_case;

    use super::*;

    #[test_case(0, vec ! [])]
    #[test_case(1, vec ! [HashMap::from([(Penny, 1)])])]
    #[test_case(2, vec ! [HashMap::from([(Penny, 2)])])]
    #[test_case(3, vec ! [HashMap::from([(Penny, 3)])])]
    #[test_case(4, vec ! [HashMap::from([(Penny, 4)])])]
    fn test_change_is_only_pennies(cents: usize, expected: Vec<HashMap<Coin, usize>>) {
        assert_eq!(make_changes(cents), expected);
    }

    #[test]
    fn change_of_5_cents() {
        let expected = vec![HashMap::from([(Nickel, 1)]), HashMap::from([(Penny, 5)])];
        assert_eq!(make_changes(5), expected);
    }

    #[test]
    fn change_of_9_cents() {
        let expected = vec![
            HashMap::from([(Nickel, 1), (Penny, 4)]),
            HashMap::from([(Penny, 9)]),
        ];
        assert_eq!(make_changes(9), expected);
    }

    #[test]
    fn change_of_10_cents() {
        let expected = vec![
            HashMap::from([(Dime, 1)]),
            HashMap::from([(Nickel, 2)]),
            HashMap::from([(Nickel, 1), (Penny, 5)]),
            HashMap::from([(Penny, 10)]),
        ];
        assert_eq!(make_changes(10), expected)
    }

    #[test]
    fn change_of_14_cents() {
        let expected = vec![
            HashMap::from([(Dime, 1), (Penny, 4)]),
            HashMap::from([(Nickel, 2), (Penny, 4)]),
            HashMap::from([(Nickel, 1), (Penny, 9)]),
            HashMap::from([(Penny, 14)]),
        ];
        assert_eq!(make_changes(14), expected)
    }

    #[test]
    fn change_of_15_cents() {
        let expected = vec![
            HashMap::from([(Dime, 1), (Nickel, 1)]),
            HashMap::from([(Dime, 1), (Penny, 5)]),
            HashMap::from([(Nickel, 3)]),
            HashMap::from([(Nickel, 2), (Penny, 5)]),
            HashMap::from([(Nickel, 1), (Penny, 10)]),
            HashMap::from([(Penny, 15)]),
        ];
        assert_eq!(make_changes(15), expected)
    }

    #[test]
    fn change_of_24_cents() {
        let expected = vec![
            HashMap::from([(Dime, 2), (Penny, 4)]),
            HashMap::from([(Dime, 1), (Nickel, 2), (Penny, 4)]),
            HashMap::from([(Dime, 1), (Nickel, 1), (Penny, 9)]),
            HashMap::from([(Dime, 1), (Penny, 14)]),
            HashMap::from([(Nickel, 4), (Penny, 4)]),
            HashMap::from([(Nickel, 3), (Penny, 9)]),
            HashMap::from([(Nickel, 2), (Penny, 14)]),
            HashMap::from([(Nickel, 1), (Penny, 19)]),
            HashMap::from([(Penny, 24)]),
        ];
        assert_eq!(make_changes(24), expected)
    }

    #[test]
    fn change_of_25_cents() {
        let expected = vec![
            HashMap::from([(Quarter, 1)]),
            HashMap::from([(Dime, 2), (Nickel, 1)]),
            HashMap::from([(Dime, 2), (Penny, 5)]),
            HashMap::from([(Dime, 1), (Nickel, 3)]),
            HashMap::from([(Dime, 1), (Nickel, 2), (Penny, 5)]),
            HashMap::from([(Dime, 1), (Nickel, 1), (Penny, 10)]),
            HashMap::from([(Dime, 1), (Penny, 15)]),
            HashMap::from([(Nickel, 5)]),
            HashMap::from([(Nickel, 4), (Penny, 5)]),
            HashMap::from([(Nickel, 3), (Penny, 10)]),
            HashMap::from([(Nickel, 2), (Penny, 15)]),
            HashMap::from([(Nickel, 1), (Penny, 20)]),
            HashMap::from([(Penny, 25)]),
        ];
        assert_eq!(make_changes(25), expected)
    }

    #[test_case(50, 49)]
    #[test_case(100, 242)]
    fn test_large_value_of_changes(cents: usize, expected_length: usize) {
        let changes = make_changes(cents);
        assert_eq!(changes.len(), expected_length);
    }
}
