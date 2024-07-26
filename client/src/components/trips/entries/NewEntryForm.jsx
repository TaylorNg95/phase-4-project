import {useContext, useState} from 'react'
import { UserContext } from '../../../context/UserContext'
import { EntryContext } from '../../../context/EntryContext'

function NewEntryForm({trip}) {
  const {user} = useContext(UserContext)
  const {entries, setEntries} = useContext(EntryContext)

  const initialFormData = {
    date: '',
    miles: '',
    user_id: user.id,
    trip_id: trip.id
  }
  
  const [formData, setFormData] = useState(initialFormData)

  function handleChange(e){
    const new_key = e.target.name
    const new_value = e.target.value
    setFormData({
        ...formData, [new_key]: new_value
    })
  }

  function handleSubmit(e) {
    e.preventDefault()
    fetch(`/api/entries`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (response.status == 201) {
            return response.json()
        } else if (response.status == 422) {
            return response.json().then(error => {
                return Promise.reject(error)
            })
        }
    })
    .then(entry => {
      console.log(entry)
      setEntries([...entries, entry])
      setFormData(initialFormData)
    })
  }

  return (
    <>
      <div>NewEntryForm</div>
      <form onSubmit={handleSubmit}>
      <label>Date (mm-dd-yy): <input type='string' name='date' value={formData.date} onChange={handleChange}/></label><br />
      <label>Miles: <input type='number' step='0.1' name='miles' value={formData.miles} onChange={handleChange}/></label><br />
      <input type='submit' value='Add New Entry'/>
      </form>
    </>
  )
}

export default NewEntryForm