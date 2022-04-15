import React, { useState, useEffect } from 'react';
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg';
import { useNavigate } from 'react-router-dom';

import { useParams } from 'react-router-dom';

const NotePage = () => {
  const navigate = useNavigate();
  let [note, setNote] = useState(null);

  const params = useParams();
  const noteId = params.id;

  useEffect(() => {
    getNote();
  }, [noteId]);

  let getNote = async () => {
    if (noteId === 'new') return;
    let response = await fetch(`/api/notes/${noteId}/`);
    let data = await response.json();
    setNote(data);
  };

  let updateNote = async () => {
    fetch(`/api/notes/${noteId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(note),
    });
  };

  let createNote = async () => {
    fetch('/api/notes/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(note),
    });
  };

  let deleteNote = async () => {
    fetch(`/api/notes/${noteId}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    navigate('/');
  };

  let handleSubmit = () => {
    console.log(note);
    if (noteId !== 'new' && note.body === '') {
      deleteNote();
    } else if (noteId !== 'new') {
      updateNote();
    } else if (noteId === 'new' && note.body !== '') {
      createNote();
    }
    navigate('/');
  };

  const handleChange = (event) => {
    setNote((prevState) => {
      return { ...prevState, body: event.target.value };
    });
  };

  return (
    <div className="note">
      <div className="note-header">
        <h3>
          <ArrowLeft onClick={handleSubmit} />
        </h3>
        {noteId !== 'new' ? (
          <button onClick={deleteNote}>Delete</button>
        ) : (
          <button onClick={handleSubmit}>Done</button>
        )}
      </div>
      <textarea onChange={handleChange} value={note?.body}></textarea>
    </div>
  );
};

export default NotePage;
