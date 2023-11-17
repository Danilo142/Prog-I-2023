import React from 'react'

export const Card = (props) => {
  return (
    <div>
        <div className="card" style={{ width: "15rem" }}>
            <img src={require(`../imagenes/${props.imagen}`) } 
                  class="card-img-top" alt="..." 
                  style={{height:"235px", width: "235px"}}  
            />
            <div class="card-body">
                <h5 class="card-title">{props.titulo}</h5>
                <p class="card-text">{props.descripcion}</p>
            </div>
        </div>
    </div>
  )
}