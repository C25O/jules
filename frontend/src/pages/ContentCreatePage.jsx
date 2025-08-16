import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import {
  Container,
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Box,
  Paper,
  TextField,
  Button,
  CircularProgress,
  Alert,
  Checkbox,
  FormControlLabel,
  Stepper,
  Step,
  StepLabel,
} from '@mui/material';

// A helper function to render the correct input based on field type
const renderField = (field, value, handleChange) => {
  const commonProps = {
    key: field.id,
    name: String(field.id),
    label: field.name,
    fullWidth: true,
    margin: "normal",
    required: field.required,
  };

  switch (field.data_type) {
    case 'Rich Text':
      return <TextField {...commonProps} value={value || ''} onChange={handleChange} multiline rows={5} />;
    case 'Boolean':
      return (
        <FormControlLabel
          control={
            <Checkbox
              name={String(field.id)}
              checked={!!value}
              onChange={handleChange}
              required={field.required}
            />
          }
          label={field.name}
          sx={{ display: 'block', mt: 2 }}
        />
      );
    case 'Number':
      return <TextField {...commonProps} value={value || ''} onChange={handleChange} type="number" />;
    default: // 'Text', 'URL', etc.
      return <TextField {...commonProps} value={value || ''} onChange={handleChange} />;
  }
};


function ContentCreatePage() {
  const navigate = useNavigate();
  const [templates, setTemplates] = useState([]);
  const [selectedTemplateId, setSelectedTemplateId] = useState('');
  const [selectedTemplate, setSelectedTemplate] = useState(null);
  const [title, setTitle] = useState('');
  const [values, setValues] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeStep, setActiveStep] = useState(0);

  // Fetch all templates for the dropdown
  useEffect(() => {
    const fetchTemplates = async () => {
      try {
        setLoading(true);
        const response = await api.getTemplates();
        setTemplates(response.data);
      } catch (err) {
        setError("Failed to load templates. Is the backend running?");
      } finally {
        setLoading(false);
      }
    };
    fetchTemplates();
  }, []);

  const handleTemplateSelect = async (templateId) => {
    if (!templateId) return;
    setSelectedTemplateId(templateId);
    setLoading(true);
    setError(null);
    try {
      const response = await api.getTemplate(templateId);
      setSelectedTemplate(response.data);
      const initialValues = {};
      response.data.fields.forEach(field => {
        initialValues[field.id] = field.data_type === 'Boolean' ? false : '';
      });
      setValues(initialValues);
      setActiveStep(1); // Move to next step
    } catch (err) {
      setError("Failed to load template details.");
    } finally {
      setLoading(false);
    }
  };

  const handleValueChange = (event) => {
    const { name, value, type, checked } = event.target;
    setValues(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError(null);
    setLoading(true);

    const contentData = {
      title,
      template_id: selectedTemplateId,
      values: Object.entries(values).map(([field_id, value]) => ({
        field_id: parseInt(field_id),
        value,
      })),
    };

    try {
      await api.createContentItem(contentData);
      navigate('/content');
    } catch (err) {
      setError("Failed to create content item.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Create New Content Item
      </Typography>
      <Stepper activeStep={activeStep} sx={{ mb: 3 }}>
        <Step><StepLabel>Select Template</StepLabel></Step>
        <Step><StepLabel>Fill Content</StepLabel></Step>
      </Stepper>
      <Paper sx={{ p: 3 }}>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}

        {activeStep === 0 && (
          <FormControl fullWidth margin="normal">
            <InputLabel id="template-select-label">Choose a Template</InputLabel>
            <Select
              labelId="template-select-label"
              value={selectedTemplateId}
              label="Choose a Template"
              onChange={(e) => handleTemplateSelect(e.target.value)}
              disabled={loading}
            >
              {templates.map((template) => (
                <MenuItem key={template.id} value={template.id}>
                  {template.name}
                </MenuItem>
              ))}
            </Select>
            {loading && <CircularProgress size={24} sx={{ mt: 2 }} />}
          </FormControl>
        )}

        {activeStep === 1 && selectedTemplate && (
          <Box component="form" onSubmit={handleSubmit} noValidate>
            <Typography variant="h6" gutterBottom>Template: {selectedTemplate.name}</Typography>
            <TextField
              label="Content Title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              fullWidth
              required
              margin="normal"
            />
            {selectedTemplate.fields.map(field =>
              renderField(field, values[field.id], handleValueChange)
            )}
            <Box sx={{ mt: 3, display: 'flex', justifyContent: 'space-between' }}>
              <Button onClick={() => setActiveStep(0)} variant="outlined">
                Back
              </Button>
              <Button type="submit" variant="contained" color="primary" disabled={loading}>
                {loading ? 'Creating...' : 'Create Content'}
              </Button>
            </Box>
          </Box>
        )}
      </Paper>
    </Container>
  );
}

export default ContentCreatePage;
