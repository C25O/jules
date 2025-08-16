import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import TemplateListPage from './pages/TemplateListPage';
import TemplateCreatePage from './pages/TemplateCreatePage';
import ContentListPage from './pages/ContentListPage';
import ContentCreatePage from './pages/ContentCreatePage';

function App() {
  return (
    <Layout>
      <Routes>
        {/* Redirect root path to the templates list */}
        <Route path="/" element={<Navigate to="/templates" replace />} />

        <Route path="/templates" element={<TemplateListPage />} />
        <Route path="/templates/new" element={<TemplateCreatePage />} />
        <Route path="/content" element={<ContentListPage />} />
        <Route path="/content/new" element={<ContentCreatePage />} />
      </Routes>
    </Layout>
  );
}

export default App;
