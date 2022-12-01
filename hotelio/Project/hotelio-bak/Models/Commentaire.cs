namespace hotelio.Models
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    public partial class Commentaire
    {
        [Key]
        public int idCommentaire { get; set; }

        [Column("Commentaire")]
        [Required]
        [StringLength(500)]
        public string Commentaire1 { get; set; }

        public int? idHotel { get; set; }

        public int? idUser { get; set; }

        public virtual Hotel Hotel { get; set; }

        public virtual User User { get; set; }
    }
}
