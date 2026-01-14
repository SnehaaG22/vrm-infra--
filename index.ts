import express from "express";
const app = express();
app.use(express.json());

app.get("/", (req, res) => res.send("Backend Sneha working"));

app.listen(3000, () => console.log("Server running on http://localhost:3000"));
