import express from 'express';
import mongoose from 'mongoose';
import { userRouter } from './routes/userRoutes';
import path from 'path';

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware to parse JSON
app.use(express.json());

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Use routes
app.use('/api', userRouter);

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/insta-insights', {
}).then(() => {
  console.log('Connected to MongoDB');
}).catch((error) => {
  console.error('Error connecting to MongoDB:', error);
});

// Root route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
