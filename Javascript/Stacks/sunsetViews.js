function sunsetViews(buildings, direction) {
  var candidateBuildings = [];
  var startIdx = direction === 'East' ? 0 : buildings.length - 1;
  var step = direction === 'East' ? 1 : -1;
  var idx = startIdx;

  while (idx >= 0 && idx < buildings.length) {
    var buildingsHeight = buildings[idx];

    while (candidateBuildings.length > 0 && buildings[candidateBuildings[candidateBuildings.length - 1]] <= buildingsHeight) {
      candidateBuildings.pop();
    }

    candidateBuildings.push(idx);
    idx = idx + step;
  }

  if (direction === 'West') return candidateBuildings.reverse();
  return candidateBuildings;
}

// Call the function
var buildings = [3, 5, 4, 4, 3, 1, 3, 2];
var direction = 'EAST'
var output = sunsetViews(buildings, direction);
console.log('👋 Output', output); //     _
//    | |_ _
//   _| | | |_   _
//  | | | | | | | |_
//  | | | | | |_| | |
// _|_|_|_|_|_|_|_|_|_