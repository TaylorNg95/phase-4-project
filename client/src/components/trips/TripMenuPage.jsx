import {useContext} from 'react'
import { TripContext } from '../../context/TripContext'
import TripMenuCard from './TripMenuCard'

function TripMenuPage() {
  const {trips} = useContext(TripContext)

  return (
    <>
      <h2>TripMenuPage</h2>
      <div>
        {trips.map(trip => <TripMenuCard key={trip.id} trip={trip}/>)}
      </div>
    </>
  )
}

export default TripMenuPage