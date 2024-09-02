import mongoose from 'mongoose';

const userSchema = new mongoose.Schema({
  username: String,
  full_name: String,
});

const User = mongoose.model('User', userSchema);

export { User };
