# Free Hosting Deployment Guide - Render

This guide will help you deploy your Django website to Render for free with automatic GitHub deployment.

## Why Render?

- ✅ **100% Free** for static sites and web services
- ✅ **Automatic deployments** from GitHub
- ✅ **Easy setup** - just connect your GitHub repo
- ✅ **Free SSL certificate** included
- ✅ **No credit card required**

## Prerequisites

1. Your project is already on GitHub ✅
2. You have a Render account (we'll create one)

## Step-by-Step Deployment

### Step 1: Create a Render Account

1. Go to [https://render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Sign up with your GitHub account (recommended for easy integration)

### Step 2: Create a New Web Service

1. Once logged in, click **"New +"** button
2. Select **"Web Service"**
3. Connect your GitHub account if you haven't already
4. Find and select your repository: `Anowar Engineering Website` (or whatever you named it)

### Step 3: Configure Your Service

Fill in the following settings:

- **Name**: `anowar-engineering-website` (or any name you prefer)
- **Region**: Choose closest to you (e.g., `Oregon (US West)`)
- **Branch**: `main` (or `master` if that's your default branch)
- **Root Directory**: Leave empty (or `.` if required)
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn company_website.wsgi:application`

### Step 4: Set Environment Variables

Click on **"Advanced"** and add these environment variables:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.11.4` | Must match runtime.txt |
| `SECRET_KEY` | `[Generate a random string]` | See below for generator |
| `DEBUG` | `False` | Always False for production |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` | Replace with your actual Render URL |

**To generate a SECRET_KEY:**
- You can use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- Or use an online Django secret key generator

### Step 5: Choose Plan

- Select **"Free"** plan
- Click **"Create Web Service"**

### Step 6: Wait for Deployment

Render will:
1. Clone your repository
2. Run the build script (`build.sh`)
3. Start your application
4. Provide you with a URL like: `https://anowar-engineering-website.onrender.com`

**First deployment takes 5-10 minutes.**

### Step 7: Run Initial Setup

Once deployed, you need to:

1. **Create a superuser** (for admin access):
   - Go to your Render dashboard
   - Click on your service
   - Go to **"Shell"** tab
   - Run: `python manage.py createsuperuser`
   - Follow the prompts

2. **Access your site**:
   - Your site will be live at: `https://your-app-name.onrender.com`
   - Admin panel: `https://your-app-name.onrender.com/admin/`

## Automatic Deployments

🎉 **That's it!** Now whenever you push changes to your GitHub repository:
- Render automatically detects the changes
- Rebuilds your application
- Deploys the new version
- Your site updates automatically!

## Important Notes

### Media Files (Uploaded Images)

⚠️ **Important**: On Render's free tier, uploaded media files are stored temporarily and may be lost when the service restarts. For production, consider:

1. **Cloud Storage** (Recommended):
   - Use AWS S3, Cloudinary, or similar
   - Update settings to use cloud storage for media files

2. **For now**: Your existing media files in the repo will work, but new uploads may not persist.

### Database

- SQLite is fine for the free tier
- For production with many users, consider upgrading to PostgreSQL (Render offers free PostgreSQL too)

### Free Tier Limitations

- Service may spin down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds (cold start)
- 750 hours/month free (enough for 24/7 operation)

## Troubleshooting

### Build Fails

- Check the build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version matches `runtime.txt`

### Static Files Not Loading

- Make sure `collectstatic` runs in build script ✅ (already included)
- Check that `STATIC_ROOT` is set correctly ✅ (already configured)

### 500 Error

- Check logs in Render dashboard
- Verify environment variables are set correctly
- Ensure `ALLOWED_HOSTS` includes your Render URL

### Can't Access Admin

- Make sure you created a superuser (Step 7)
- Check that migrations ran successfully

## Alternative: Railway (Another Free Option)

If you prefer Railway:

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Django and sets it up
6. Add environment variables in the Variables tab
7. Deploy!

Railway gives $5 free credit monthly (enough for small projects).

## Need Help?

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- Check your build/deploy logs in Render dashboard

---

**Your site will automatically update every time you push to GitHub! 🚀**

