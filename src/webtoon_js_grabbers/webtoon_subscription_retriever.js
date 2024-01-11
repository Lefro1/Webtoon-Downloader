const seriesList = [];

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

  // Create the formatted entry and push it to the list
  const formattedEntry = `${seriesName}|${referenceURL}`;
  seriesList.push(formattedEntry);
}

// Print the entries in a single column
console.log(seriesList.join('\n'));
