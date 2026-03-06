// Bug 5 - Syntax error (async/await misuse)
// Intended Behavior: Fetch user data from an API endpoint and return the user's name in uppercase. The function is intended to use `async/await` so callers can `await` the final string result. 
// Issue Type: Syntax error (async/await misuse). 

async function fetchUserNameUpper(userId) {
  const url = `https://api.example.com/users/${userId}`;

  // BUG: 'await' is used inside a non-async function.
  const response = await fetch(url);
  const user = await response.json();

  return user.name.toUpperCase();
}

// Example usage (won't run because of the syntax error above)
console.log(fetchUserNameUpper(42));
