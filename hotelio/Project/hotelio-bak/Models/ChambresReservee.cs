namespace hotelio.Models
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("ChambresReservee")]
    public partial class ChambresReservee
    {
        [Key]
        [Column(Order = 0)]
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int idReservation { get; set; }

        [Key]
        [Column(Order = 1)]
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int idChambre { get; set; }

        public int nbrChambreReservee { get; set; }

        public virtual Chambre Chambre { get; set; }

        public virtual Reservation Reservation { get; set; }
    }
}
