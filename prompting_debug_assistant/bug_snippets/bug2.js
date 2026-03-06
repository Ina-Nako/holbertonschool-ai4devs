// Fetch user data and process it
async function fetchUserData(userId) {
    try {
        const response = await fetch(`https://api.example.com/users/${userId}`);
        const data = response.json();  // Missing await here!
        
        console.log("Username: " + data.name);
        console.log("Email: " + data.email);
        
        return data;
    } catch (error) {
        console.log("Error fetching user: " + error);
    }
}

// Test
fetchUserData(42);