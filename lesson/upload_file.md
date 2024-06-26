#Move File Upload

**_import_**
```python
import os
```

```python
UPLOAD_FOLDER = 'image'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
```

```python
file = request.files['file']
# Option 1
file.save('/image', f.filename)
# Option 2
file.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/product', file.filename))
```

```python
return redirect(url_for('add_product', name=file.filename))
```

### Delete file upload
```python
os.remove(os.path.join(app.config['UPLOADED_ITEMS_DEST'], your_filename))
```
