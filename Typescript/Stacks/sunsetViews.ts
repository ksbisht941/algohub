export enum Direction {
    East = 'EAST',
    West = 'WEST',
}

export function sunsetViews(buildings: number[], direction: Direction) {
    let candidateBuildings = [];

    const startIdx = direction === Direction.East ? 0 : buildings.length - 1;
    const step = direction === Direction.East ? 1 : -1;

    let idx = startIdx;

    while (idx >= 0 && idx < buildings.length) {
        const buildingsHeight = buildings[idx];

        while (
            candidateBuildings.length > 0 && 
            buildings[candidateBuildings[candidateBuildings.length - 1]] <= buildingsHeight
        ) {
            candidateBuildings.pop();
        }

        candidateBuildings.push(idx);

        idx = idx + step;
    }

    if (direction === Direction.West) return candidateBuildings.reverse();

    return candidateBuildings;
}


// Call the function
const buildings: number[] = [3, 5, 4, 4, 3, 1, 3, 2]
const direction: Direction = Direction.West

const output = sunsetViews(buildings, direction)
console.log('👋 Output', output)


//     _
//    | |_ _
//   _| | | |_   _
//  | | | | | | | |_
//  | | | | | |_| | |
// _|_|_|_|_|_|_|_|_|_
