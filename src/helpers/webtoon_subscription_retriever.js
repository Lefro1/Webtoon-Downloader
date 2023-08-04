// Initialize an empty map to store the series names and URLs
const seriesMap = new Map();

// Get all entries in the unordered lists
const originals = document.querySelectorAll('#_webtoonList li');
const canvas = document.querySelectorAll('#_challengeList li');

// Merge the two NodeLists into a single array
const allEntries = [...originals, ...canvas];

// Loop through each item in the merged list
for (const listItem of allEntries) {
  // Extract the series name
  const seriesName = listItem.querySelector('p.subj').textContent;

  // Extract the reference URL
  const referenceURL = listItem.querySelector('a.card_item').getAttribute('href');

  // Add the series name and URL to the map
  seriesMap.set(seriesName, referenceURL);
}

// Print the entries in CSV format
for (const [seriesName, referenceURL] of seriesMap) {
  console.log(`${seriesName}|${referenceURL}`);
}
