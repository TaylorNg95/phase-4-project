import {useContext} from 'react'
import { UserContext } from '../../../context/UserContext'

function EntryItem({entry}) {

  const {deleteEntry} = useContext(UserContext)

  function handleEdit(id) {
    console.log('handling edit')
  }

  return (
    <div>
      {entry.date} || {entry.miles} mile{entry.miles == 1.0 ? '' : 's'}
      <button onClick={() => handleEdit(entry.id)}>Edit</button><button onClick={() => deleteEntry(entry.id)}>Delete</button>
    </div>
  )
}

export default EntryItem