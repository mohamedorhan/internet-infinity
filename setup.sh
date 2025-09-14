#!/bin/bash
# ====================================================
#  Internet ∞ Infinity - Setup Script
#  Author: Mohamed Orhan Zeinel
#  Description: Quick environment setup for the
#               Next-Generation Internet project
# ====================================================

echo "🌐 Setting up Internet ∞ Infinity..."

# Step 1: Check Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found. Please install Python 3.9+ first."
    exit 1
fi
echo "✅ Python3 detected: $(python3 --version)"

# Step 2: Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "🔄 Virtual environment already exists, skipping..."
fi

# Step 3: Activate environment
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# Step 4: Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Step 5: Install requirements
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found, skipping dependency installation."
fi

# Step 6: Create necessary folders if missing
mkdir -p logs state data/samples

# Step 7: Initialize state files if not present
if [ ! -f "state/session_state.json" ]; then
    echo "{}" > state/session_state.json
    echo "📝 Created empty session_state.json"
fi

# Step 8: Done
echo "✅ Setup completed successfully!"
echo ""
echo "👉 To run the system:"
echo "   source venv/bin/activate"
echo "   python internet_infinity.py"
echo ""