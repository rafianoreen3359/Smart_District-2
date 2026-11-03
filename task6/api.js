const USERS_API= "https://jsonplaceholder.typicode.com/users";
const POSTS_API = "https://jsonplaceholder.typicode.com/posts";
async function fetchUsers(){
const response = await fetch(USERS_API);
if(!response.ok){
    throw new Error("Unable to fetch users .");
}
return await response.json();
}
async function fetchPosts(){
    const response=await fetch(POSTS_API);
   if (!response.ok) {
    throw new Error("Unable to fetch posts.");
}

return await response.json();
}
export async function fetchDashboardData() {
const [users, posts] = await Promise.all([
fetchUsers(),
fetchPosts()
]);

return { users, posts };

}