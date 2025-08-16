import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import {
  Container,
  Typography,
  TextField,
  Button,
  Box,
  Paper,
  IconButton,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Checkbox,
  FormControlLabel,
  Grid,
  Alert,
} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import DeleteIcon from '@mui/icons-material/Delete';

// These are the basic data types supported by the system for now.
const availableDataTypes = [
  'Text', 'Rich Text', 'Date/DateTime', 'Number', 'Boolean', 'Image', 'URL'
];

function TemplateCreatePage() {
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [fields, setFields] = useState([{ name: '', data_type: 'Text', required: true }]);
  const [error, setError] = useState(null);

  const handleAddField = () => {
    setFields([...fields, { name: '', data_type: 'Text', required: true }]);
  };

  const handleRemoveField = (index) => {
    const newFields = fields.filter((_, i) => i !== index);
    setFields(newFields);
  };

  const handleFieldChange = (index, event) => {
    const newFields = [...fields];
    const { name, value, type, checked } = event.target;
    newFields[index][name] = type === 'checkbox' ? checked : value;
    setFields(newFields);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError(null);

    // Basic validation
    if (!name.trim()) {
      setError("Template Name is required.");
      return;
    }
    for (const field of fields) {
      if (!field.name.trim()) {
        setError("All fields must have a name.");
        return;
      }
    }

    try {
      const templateData = { name, description, fields };
      await api.createTemplate(templateData);
      navigate('/templates'); // Redirect on success
    } catch (err) {
      const errorMsg = err.response?.data?.detail || 'An unknown error occurred.';
      setError(`Failed to create template: ${errorMsg}`);
      console.error(err);
    }
  };

  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Create New Page Template
      </Typography>
      <Paper sx={{ p: { xs: 2, md: 3 } }}>
        <Box component="form" onSubmit={handleSubmit} noValidate>
          <TextField
            label="Template Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            fullWidth
            required
            margin="normal"
          />
          <TextField
            label="Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            fullWidth
            margin="normal"
            multiline
            rows={3}
          />

          <Typography variant="h6" sx={{ mt: 3, mb: 1 }}>Fields</Typography>
          {fields.map((field, index) => (
            <Paper key={index} sx={{ p: 2, mb: 2, bgcolor: 'grey.50' }}>
              <Grid container spacing={2} alignItems="center">
                <Grid item xs={12} sm={4}>
                  <TextField
                    label="Field Name"
                    name="name"
                    value={field.name}
                    onChange={(e) => handleFieldChange(index, e)}
                    fullWidth
                    required
                    size="small"
                  />
                </Grid>
                <Grid item xs={12} sm={4}>
                  <FormControl fullWidth size="small">
                    <InputLabel>Data Type</InputLabel>
                    <Select
                      name="data_type"
                      value={field.data_type}
                      onChange={(e) => handleFieldChange(index, e)}
                    >
                      {availableDataTypes.map(type => (
                        <MenuItem key={type} value={type}>{type}</MenuItem>
                      ))}
                    </Select>
                  </FormControl>
                </Grid>
                <Grid item xs={6} sm={2}>
                  <FormControlLabel
                    control={
                      <Checkbox
                        name="required"
                        checked={field.required}
                        onChange={(e) => handleFieldChange(index, e)}
                      />
                    }
                    label="Required"
                  />
                </Grid>
                <Grid item xs={6} sm={2} sx={{ textAlign: 'right' }}>
                  <IconButton onClick={() => handleRemoveField(index)} aria-label="delete field" color="error">
                    <DeleteIcon />
                  </IconButton>
                </Grid>
              </Grid>
            </Paper>
          ))}

          <Button
            startIcon={<AddIcon />}
            onClick={handleAddField}
            variant="outlined"
            sx={{ mt: 1 }}
          >
            Add Field
          </Button>

          {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}

          <Box sx={{ mt: 3, display: 'flex', justifyContent: 'flex-end', gap: 1 }}>
             <Button onClick={() => navigate('/templates')} variant="outlined">
              Cancel
            </Button>
            <Button type="submit" variant="contained" color="primary">
              Create Template
            </Button>
          </Box>
        </Box>
      </Paper>
    </Container>
  );
}

export default TemplateCreatePage;
