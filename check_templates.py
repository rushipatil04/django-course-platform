import os

print("Checking template files...")

# Check if templates directory exists
if os.path.exists('templates'):
    print("✅ templates/ directory exists")
    
    # List all files in templates
    for root, dirs, files in os.walk('templates'):
        for file in files:
            filepath = os.path.join(root, file)
            size = os.path.getsize(filepath)
            print(f"  📄 {filepath} ({size} bytes)")
else:
    print("❌ templates/ directory NOT FOUND!")

# Check settings
print("\nChecking settings.py TEMPLATES configuration...")
with open('courseplatform/settings.py', 'r') as f:
    content = f.read()
    if "'DIRS': [BASE_DIR / 'templates']" in content or '"DIRS": [BASE_DIR / "templates"]' in content:
        print("✅ TEMPLATES DIRS is configured correctly")
    else:
        print("❌ TEMPLATES DIRS might not be configured correctly")