import axios from 'axios';

// Create an axios instance with a base URL.
// This assumes the backend API is running on port 8000 during development.
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// --- Template Functions ---

/**
 * Fetches all page templates.
 * @returns {Promise} A promise that resolves to the list of templates.
 */
export const getTemplates = () => {
  return apiClient.get('/templates/');
};

/**
 * Fetches a single page template by its ID.
 * @param {number} id The ID of the template.
 * @returns {Promise} A promise that resolves to the template data.
 */
export const getTemplate = (id) => {
  return apiClient.get(`/templates/${id}`);
};

/**
 * Creates a new page template.
 * @param {object} templateData The data for the new template.
 * @returns {Promise} A promise that resolves to the newly created template data.
 */
export const createTemplate = (templateData) => {
  return apiClient.post('/templates/', templateData);
};


// --- Content Functions ---

/**
 * Fetches all content items.
 * @returns {Promise} A promise that resolves to the list of content items.
 */
export const getContentItems = () => {
  return apiClient.get('/content/');
};

/**
 * Fetches a single content item by its ID.
 * @param {number} id The ID of the content item.
 * @returns {Promise} A promise that resolves to the content item data.
 */
export const getContentItem = (id) => {
  return apiClient.get(`/content/${id}`);
};

/**
 * Creates a new content item.
 * @param {object} contentData The data for the new content item.
 * @returns {Promise} A promise that resolves to the newly created content item data.
 */
export const createContentItem = (contentData) => {
  return apiClient.post('/content/', contentData);
};

/**
 * Fetches a content item formatted as Markdown.
 * @param {number} id The ID of the content item.
 * @returns {Promise} A promise that resolves to the Markdown string.
 */
export const getContentItemAsMarkdown = (id) => {
  return apiClient.get(`/content/${id}/markdown`);
};

// Default export for convenience
const api = {
  getTemplates,
  getTemplate,
  createTemplate,
  getContentItems,
  getContentItem,
  createContentItem,
  getContentItemAsMarkdown,
};

export default api;
