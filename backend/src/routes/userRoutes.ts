import { Router, Request, Response } from 'express';
import { User } from '../models/User';
import { DontFollowMeBack } from '../models/DontFollowMeBack';
import { IDontFollowBack } from '../models/IDontFollowBack';

const router = Router();

// Endpoint to store Instagram data
router.post('/save-instagram-data', async (req: Request, res: Response) => {
  try {
    const { followers, followings, dontFollowMeBack, iDontFollowBack } = req.body;

    // Save followers and followings to User collection
    await User.insertMany(followers);
    await User.insertMany(followings);

    // Save 'don't follow me back' to their collection
    await DontFollowMeBack.insertMany(dontFollowMeBack);

    // Save 'I don't follow back' to their collection
    await IDontFollowBack.insertMany(iDontFollowBack);

    res.status(201).send('Data saved successfully!');
  } catch (error) {
    console.error('Error saving data:', error);
    res.status(500).send('Server error');
  }
});

// Endpoint to fetch all followers
router.get('/followers', async (req: Request, res: Response) => {
  try {
    const followers = await User.find({}); // Adjust the query as needed
    res.json(followers);
  } catch (error) {
    console.error('Error fetching followers:', error);
    res.status(500).send('Server error');
  }
});

// Endpoint to fetch users who don’t follow back
router.get('/dont-follow-me-back', async (req: Request, res: Response) => {
  try {
    const users = await DontFollowMeBack.find({});
    res.json(users);
  } catch (error) {
    console.error('Error fetching users who don’t follow me back:', error);
    res.status(500).send('Server error');
  }
});

// Endpoint to fetch users I don’t follow back
router.get('/i-dont-follow-back', async (req: Request, res: Response) => {
  try {
    const users = await IDontFollowBack.find({});
    res.json(users);
  } catch (error) {
    console.error('Error fetching users I don’t follow back:', error);
    res.status(500).send('Server error');
  }
});

export { router as userRouter };
