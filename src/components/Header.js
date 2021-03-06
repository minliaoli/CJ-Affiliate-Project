import React, { Component } from 'react'

export class Header extends Component {
    render() {
        return (
            <div>
                <nav className="navbar navbar-dark bg-success color-green">
                    <img src="../new-cj-logo-icon.svg" href="../" alt="CJ Affiliate Logo" width={90} height={90} />
                    
                    <a className="navbar-brand" href="../">Offer Matcher</a>

                    <button className="navbar-toggler" id="navbarDropdownMenuLink" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    
                    <div className="dropdown-menu dropdown-menu-right " aria-labelledby="navbarDropdownMenuLink">
                            <a className="dropdown-item" href="../enteryoutube">Enter Youtube video URL</a>
                            <div className="dropdown-divider"></div>
                            <a className="dropdown-item" href="../enterurl">Enter blog URL</a>
                            <a className="dropdown-item" href="../entertext">Enter blog text</a>
                            <a className="dropdown-item" href="../entertype">Select from keywords</a>
                    </div>
                </nav>
            </div>

        )
    }
}

export default Header

