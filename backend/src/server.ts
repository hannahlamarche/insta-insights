import express, { Request, Response } from 'express';
import mongoose from 'mongoose';
import axios from 'axios';

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware to parse JSON
app.use(express.json());

// Root route
app.get('/', (req: Request, res: Response) => {
  res.send('Hello World!');
});

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/insta-insights', {
}).then(() => {
  console.log('Connected to MongoDB');
}).catch((error) => {
  console.error('Error connecting to MongoDB:', error);
});

// Define Mongoose schemas and models
const userSchema = new mongoose.Schema({
  username: String,
  full_name: String,
});

const User = mongoose.model('User', userSchema);

// Example endpoint to store Instagram data
app.post('/save-instagram-data', async (req: Request, res: Response) => {
  try {
    const { followers, followings, dontFollowMeBack, iDontFollowBack } = req.body;

    // Save each set of data to MongoDB
    await User.insertMany(followers);
    await User.insertMany(followings);
    await User.insertMany(dontFollowMeBack);
    await User.insertMany(iDontFollowBack);

    res.status(201).send('Data saved successfully!');
  } catch (error) {
    console.error(error);
    res.status(500).send('Server error');
  }
});

// Start the server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
