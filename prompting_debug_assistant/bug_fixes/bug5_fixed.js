// Bug 5 Fixed - Syntax error (async/await misuse)
// Intended behavior: fetch user JSON and return the user's name uppercased.
// Fix: ensured the enclosing function is declared async so await is valid;
//      caller uses .then() to handle the returned Promise.

async function fetchUserNameUpper(userId) {
  const url = `https://api.example.com/users/${userId}`;

  const response = await fetch(url);   // valid: inside an async function
  const user = await response.json();

  return user.name.toUpperCase();
}

// --- Unit test with a mocked fetch ---
globalThis.fetch = async () => ({
  json: async () => ({ name: "Ada Lovelace" }),
});

fetchUserNameUpper(42).then((result) => {
  console.assert(result === "ADA LOVELACE", `Expected "ADA LOVELACE", got "${result}"`);
  console.log("All tests passed.");
});
